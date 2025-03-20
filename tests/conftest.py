import ipaddress
import random
from dataclasses import dataclass, field
import pytest
from pytest import FixtureRequest


def random_ipv4():
    return ipaddress.IPv4Address(random.randint(0, (2**32) - 1))


def random_port():
    return random.randint(1, 60000)


@dataclass
class CGNVariables:
    host: str = field(default_factory=random_ipv4)
    vrf_id: int = 0
    protocol: int = 7
    src_ip: str = field(default_factory=random_ipv4)
    src_port: int = field(default_factory=random_port)
    x_ip: str = field(default_factory=random_ipv4)
    x_port: int = field(default_factory=random_port)
    dst_ip: str = field(default_factory=random_ipv4)
    dst_port: int = field(default_factory=random_port)


@pytest.fixture(scope="module")
def cgn_variables(request: FixtureRequest) -> CGNVariables:
    return CGNVariables()
