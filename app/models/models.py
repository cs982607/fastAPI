from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey,
	Time
)
from sqlalchemy.orm import relationship
from common.guid_type import GUID
from database.database import Base


class BaseModels(object):
	id = Column(GUID, primary_key=True, index=True)
	created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
	updated_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())

class Rule(Base, BaseModels):
	__tablename__ = "rules"
	time = Column(Time, nullable=False)

	users = relationship("Users", back_populates="rule")


class Users(Base, BaseModels):
	__tablename__ = "users"

	name = Column(String(length=10), nullable=False)
	mobile = Column(Integer, nullable=False)
	team = Column(String(length=20), nullable=False) 
	rule_id = Column(GUID, ForeignKey("rules.id"), nullable=False)
	
	rule = relationship("Rule", back_populates="users")
	worklogs = relationship("Worklog", back_populates="user")


class Worklog(Base, BaseModels):
	__tablename__ = "worklogs"

	user_id = Column(GUID, ForeignKey("users.id"), nullable=False)
	timestamp_in = Column(DateTime, nullable=False)
	timestamp_out = Column(DateTime, nullable=False)

	user = relationship("Users", back_populates="worklogs")


