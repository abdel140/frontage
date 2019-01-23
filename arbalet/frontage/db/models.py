import datetime

# from server.extensions import db
from uuid import uuid4
from db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean


def cln_str(s):
    if s:
        return s.replace(
            "'",
            "").replace(
            '\\',
            '').replace(
            '%',
            '').replace(
                ';',
            '')
    return ''

class FappModel(Base):
    __tablename__ = 'fapp'

    uniqid = Column(String(36), primary_key=True)
    name = Column(String(36), unique=True)
    is_scheduled = Column(Boolean)
    default_params = Column(String(4096))
    position = Column(Integer)

    def __init__(self, app_name, is_scheduled=False):
        self.uniqid = str(uuid4())
        self.position = 0
        self.name = app_name
        self.is_scheduled = is_scheduled
        self.default_params = '{}'

    def __repr__(self):
        return '<Fapp %r (%r) (%r) (%r)>' % (
            self.uniqid, self.is_scheduled, self.position, self.default_params)


class ConfigModel(Base):
    __tablename__ = 'configmodel'

    uniqid = Column(String(36), primary_key=True)


    time_on = Column(String(10))             # On time, which can be formatted as %H:%m or "sunrise", "sunset"
    time_off = Column(String(10))            # On time, which can be formatted as %H:%m or "sunrise", "sunset"
    offset_time_on = Column(Integer)         # Offset in seconds for actual ON time, with respect to time_on
    offset_time_off = Column(Integer)        # Offset in seconds for actual OFF time, with respect to time_off
    state = Column(String(36))               # "on", "off", "scheduled"
    expires_delay = Column(Integer)
    default_app_lifetime = Column(Integer)

    admin_login = Column(String(36))
    admin_hash = Column(String(512))

    def __init__(self):
        # Default values when initializing a new database
        self.uniqid = str(uuid4())
        self.state = 'scheduled'
        self.time_on = "sunset"
        self.time_off = "sunrise"
        self.offset_time_off = 0
        self.offset_time_on = 0
        self.default_app_lifetime = 15 * 60
        self.expires_delay = 90

    def __repr__(self):
        return '<ConfigModel %r (%r) (%r)>' % (
            self.uniqid, self.expires_delay, self.forced_sunset)
