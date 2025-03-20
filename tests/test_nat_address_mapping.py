from datetime import datetime
from ipaddress import IPv4Interface

from tests.conftest import CGNVariables

from cgn_ec_models.sqlmodel import (
    NATAddressMapping,
    NATEventTypeEnum,
)


def test_nat_address_mapping_valid(cgn_variables: CGNVariables):
    now = datetime.now()

    mapping = NATAddressMapping(
        timestamp=now,
        host=cgn_variables.host,
        event=NATEventTypeEnum.CREATED,
        vrf_id=cgn_variables.vrf_id,
        protocol=cgn_variables.protocol,
        src_ip=cgn_variables.src_ip,
        x_ip=cgn_variables.x_ip,
    )

    assert mapping.timestamp == now
    assert IPv4Interface(mapping.host).ip == cgn_variables.host
    assert mapping.vrf_id == cgn_variables.vrf_id
    assert IPv4Interface(mapping.src_ip).ip == cgn_variables.src_ip
    assert IPv4Interface(mapping.x_ip).ip == cgn_variables.x_ip
