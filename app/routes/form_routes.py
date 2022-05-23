from app.globals import router, database
from app.models.form_model import FormModel
from app.databases.standard_base import BaseDB


form_base = BaseDB(database['forms'], FormModel)


@router.post("/form", response_model=FormModel, tags=['users'])
async def post_form(form: FormModel):
    result = await form_base.create_one(dict(form))
    return result
