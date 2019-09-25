import logging
from http import HTTPStatus
from typing import List, Union

from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from api.server.db import get_mongo_c
from api.server.db.user_init import clear_resources_for_role, get_all_available_resource_actions
from api.server.db.role import RoleModel, DefaultRoleUUID
from api.server.utils.problems import (UnauthorizedException, UniquenessException, InvalidInputException,
                                       DoesNotExistException)
from common import mongo_helpers

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/",
            response_model=List[RoleModel], response_description="List of all roles.")
async def read_all_roles(role_col: AsyncIOMotorCollection = Depends(get_mongo_c)):
    """
    Returns a list of all roles.
    """
    return await mongo_helpers.get_all_items(role_col, RoleModel,
                                             query={"id_": {"$nin": [
                                                 DefaultRoleUUID.INTERNAL_USER.value,
                                                 DefaultRoleUUID.SUPER_ADMIN.value
                                             ]}})


@router.post("/",
             response_model=RoleModel, response_description="The newly created Role.")
async def create_role(*, role_col: AsyncIOMotorCollection = Depends(get_mongo_c),
                      new_role: RoleModel):

    return await mongo_helpers.create_item(role_col, RoleModel, new_role)

    #
    # json_data = dict(add_role)
    #
    # if not role_col.find_one({"name": add_role.name}, projection={'_id': False}):
    #     resources = add_role.resources if 'resources' in add_role else []
    #     if '/roles' in resources:
    #         resources.remove('/roles')
    #
    #     role_params = {'name': add_role.name,
    #                    'description': add_role.description if 'description' in add_role else '',
    #                    'resources': resources}
    #     new_role = RoleModel(**role_params)
    #     new_role.set_resources(resources, role_col)
    #     return new_role
    # else:
    #     # current_app.logger.warning(f"Role with name {json_data['name']} already exists")
    #     return ProblemException(
    #         HTTPStatus.BAD_REQUEST,
    #         "Could not create role.",
    #         f"Role with name {json_data['name']} already exists")


@router.get('/{role_id}',
            response_model=RoleModel, response_description="The requested Role.")
async def read_role(*, role_col: AsyncIOMotorCollection = Depends(get_mongo_c),
                    role_id: Union[int, str]):
    """
    Returns the Role for the specified role name or ID
    """
    role = await mongo_helpers.get_item(role_col, RoleModel, role_id)
    role_string = f"{role.name} ({role.id_})"
    if role.id_ in range(1, 2):
        raise UnauthorizedException("update", "role", role_string)
    else:
        return role

    # role = await role_getter(role_col, role_id=role_id)
    # if role is None:
    #     return ProblemException(
    #         HTTPStatus.BAD_REQUEST,
    #         'Could not logout.',
    #         'The identity of the refresh token does not match the identity of the authentication token.')
    # # check for internal or super_admin
    # if role.id_ != 1 or role.id_ != 2:
    #     return dict(role)
    # else:
    #     return None


@router.put('/{role_id}')
async def update_role(*, role_col: AsyncIOMotorCollection = Depends(get_mongo_c),
                      role_id: Union[int, str],
                      new_role: RoleModel):

    role: RoleModel = await mongo_helpers.get_item(role_col, RoleModel, role_id, raise_exc=False)
    if not role:
        raise DoesNotExistException("update", "Role", role_id)

    role_string = f"{role.name} ({role.id_})"

    if role.id_ in range(1, 6):
        raise UnauthorizedException("update", "role", role_string)

    if new_role.name:
        existing_user = await mongo_helpers.get_item(role_col, RoleModel, new_role.name, raise_exc=False)
        if existing_user:
            raise UniquenessException("change role for", "Role", f"{role_string} -> "
                                                                 f"{new_role.name} ({role.id_})")
        else:
            role.name = new_role.name

    if new_role.description:
        role.description = new_role.description

    if new_role.resources:
        role.resources = new_role.resources

    return await mongo_helpers.update_item(role_col, RoleModel, role_id, role)

    # role = await role_getter(role_col, role_id=role_id)
    # if role.id_ != 1 and role.id_ != 2:
    #     if 'name' in updated_role:
    #         new_name = updated_role.name
    #         role_db = role_col.find_one({"name": new_name}, projection=False)
    #         # role_db = db_session.query(Role).filter_by(name=new_name).first()
    #         if role_db is None or role_db.id_ == updated_role.id_:
    #             role.name = new_name
    #     if 'description' in updated_role:
    #         role.description = update_role.description
    #     if 'resources' in updated_role:
    #         resources = update_role.resources
    #         role.set_resources(resources, role_col)
    #     # current_app.logger.info(f"Edited role {json_data['id_']} to {json_data}")
    #     return dict(role)
    # else:
    #     return None


@router.delete('/{role_id}')
async def delete_role(*, role_col: AsyncIOMotorCollection = Depends(get_mongo_c),
                      role_id: Union[int, str]):

    role = await mongo_helpers.get_item(role_col, RoleModel, role_id, raise_exc=False)
    role_string = f"{role.rolename} ({role.id_})"

    if role.id_ in range(1, 6):
        raise UnauthorizedException("delete", "role", role_string)
    else:
        return await mongo_helpers.delete_item(role_col, RoleModel, role_id)

    # role = await role_getter(role_col, role_id=role_id)
    # if role.id_ != 1 or role.id_ != 2:
    #     r = await role_col.delete_one(role)
    #     return r
    # else:
    #     return None


@router.get('/availableresourceactions')
async def read_available_resource_actions():
    return get_all_available_resource_actions(), HTTPStatus.OK

