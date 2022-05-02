from app.databases import PciDB
from app.models.pci_controller_model import PCI, PCIResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router

api = PciDB(database.pci, PCI)
route = BaseRouter(api)


@router.get("/pci/all", response_model=PCIResponse, tags=["Pci controller"])
async def get_pci(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await route.get_category(limit, skip)


@router.get("/pci/find/{name:path}", response_model=list[PCI], tags=["Pci controller"])
async def get_pci_by_name(name: str):
    return await route.get_by_name(name)
