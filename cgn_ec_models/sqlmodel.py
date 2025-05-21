from datetime import datetime
from ipaddress import IPv4Address, IPv6Address

from pydantic import ConfigDict
from sqlmodel import (
    SQLModel,
    PrimaryKeyConstraint,
    Field,
    Column,
    SmallInteger,
    Integer,
    VARCHAR,
)
from sqlalchemy.dialects.postgresql import INET

from cgn_ec_models.enums import NATEventTypeEnum


class MetricBase(SQLModel):
    model_config = ConfigDict(use_enum_values=True)
    timestamp: datetime


class NATSessionMapping(MetricBase, table=True):
    __tablename__ = "session_mapping"
    __table_args__ = (
        PrimaryKeyConstraint(
            "timestamp", "host", "event", "src_ip", "src_port", "dst_ip", "dst_port"
        ),
        {"timescaledb_hypertable": {"time_column_name": "timestamp"}},
    )

    host: IPv4Address | IPv6Address = Field(sa_column=Column(INET))
    event: NATEventTypeEnum = Field(sa_column=Column(Integer))
    vrf_id: str | None = Field(
        default=None, sa_column=Column(VARCHAR, nullable=True)
    )
    protocol: int = Field(sa_column=Column(SmallInteger))
    src_ip: IPv4Address = Field(sa_column=Column(INET))
    src_port: int = Field(sa_column=Column(Integer))
    x_ip: IPv4Address = Field(sa_column=Column(INET))
    x_port: int = Field(sa_column=Column(Integer))
    dst_ip: IPv4Address = Field(sa_column=Column(INET))
    dst_port: int = Field(sa_column=Column(Integer))


class NATAddressMapping(MetricBase, table=True):
    __tablename__ = "address_mapping"
    __table_args__ = (
        PrimaryKeyConstraint("timestamp", "host", "event", "vrf_id", "src_ip", "x_ip"),
        {"timescaledb_hypertable": {"time_column_name": "timestamp"}},
    )

    host: IPv4Address | IPv6Address = Field(sa_column=Column(INET))
    event: NATEventTypeEnum = Field(sa_column=Column(SmallInteger))
    vrf_id: str | None = Field(
        default=None, sa_column=Column(VARCHAR, nullable=True)
    )
    src_ip: IPv4Address = Field(sa_column=Column(INET))
    x_ip: IPv4Address = Field(sa_column=Column(INET))


class NATPortMapping(MetricBase, table=True):
    __tablename__ = "port_mapping"
    __table_args__ = (
        PrimaryKeyConstraint(
            "timestamp",
            "host",
            "event",
            "protocol",
            "src_ip",
            "x_ip",
            "x_ip",
            "x_port",
        ),
        {"timescaledb_hypertable": {"time_column_name": "timestamp"}},
    )

    host: IPv4Address | IPv6Address = Field(sa_column=Column(INET))
    event: NATEventTypeEnum = Field(sa_column=Column(SmallInteger))
    vrf_id: str | None = Field(
        default=None, sa_column=Column(VARCHAR, nullable=True)
    )
    protocol: int = Field(sa_column=Column(SmallInteger))
    src_ip: IPv4Address = Field(sa_column=Column(INET))
    src_port: int = Field(sa_column=Column(Integer))
    x_ip: IPv4Address = Field(sa_column=Column(INET))
    x_port: int = Field(sa_column=Column(Integer))


class NATPortBlockMapping(MetricBase, table=True):
    __tablename__ = "port_block_mapping"
    __table_args__ = (
        PrimaryKeyConstraint(
            "timestamp",
            "host",
            "event",
            "src_ip",
            "x_ip",
            "start_port",
            "end_port",
        ),
        {"timescaledb_hypertable": {"time_column_name": "timestamp"}},
    )

    host: IPv4Address | IPv6Address = Field(sa_column=Column(INET))
    event: NATEventTypeEnum = Field(sa_column=Column(SmallInteger))
    vrf_id: str | None = Field(
        default=None, sa_column=Column(VARCHAR, nullable=True)
    )
    src_ip: IPv4Address = Field(sa_column=Column(INET))
    x_ip: IPv4Address = Field(sa_column=Column(INET))
    start_port: int = Field(sa_column=Column(Integer))
    end_port: int = Field(sa_column=Column(Integer))
