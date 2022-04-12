from common.view_model import ViewModel
from typing import Optional
from uuid import UUID

class RuleViewModel(ViewModel):
    id: UUID | None

class UserViewModel(ViewModel):
    id: UUID | None