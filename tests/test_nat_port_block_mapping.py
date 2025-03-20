from datetime import datetime
from ipaddress import IPv4Interface

from tests.conftest import CGNVariables

from cgn_ec_models.sqlmodel import (
    NATEventTypeEnum,
    NATPortBlockMapping,
)


def test_nat_port_block_mapping_valid(cgn_variables: CGNVariables):
    now = datetime.now()

    mapping = NATPortBlockMapping(
        timestamp=now,
        host=cgn_variables.host,
        event=NATEventTypeEnum.CREATED,
        vrf_id=cgn_variables.vrf_id,
        protocol=cgn_variables.protocol,
        src_ip=cgn_variables.src_ip,
        x_ip=cgn_variables.x_ip,
        start_port=20000,
        end_port=21000,
    )

    assert mapping.timestamp == now
    assert IPv4Interface(mapping.host).ip == cgn_variables.host
    assert mapping.vrf_id == cgn_variables.vrf_id
    assert IPv4Interface(mapping.src_ip).ip == cgn_variables.src_ip
    assert IPv4Interface(mapping.x_ip).ip == cgn_variables.x_ip
    assert mapping.start_port == 20000
    assert mapping.end_port == 21000
