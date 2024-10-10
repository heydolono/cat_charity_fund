from app.crud.base import CRUDBase
from models import CharityProject


class CRUDCharityProject(CRUDBase):
    pass


charityproject_crud = CRUDCharityProject(CharityProject)
