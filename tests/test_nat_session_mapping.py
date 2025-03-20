from datetime import datetime
from ipaddress import IPv4Interface

from tests.conftest import CGNVariables

from cgn_ec_models.sqlmodel import (
    NATSessionMapping,
    NATEventTypeEnum,
)


def test_nat_session_mapping_valid(cgn_variables: CGNVariables):
    now = datetime.now()

    mapping = NATSessionMapping(
        timestamp=now,
        host=cgn_variables.host,
        event=NATEventTypeEnum.CREATED,
        vrf_id=cgn_variables.vrf_id,
        protocol=cgn_variables.protocol,
        src_ip=cgn_variables.src_ip,
        src_port=cgn_variables.src_port,
        x_ip=cgn_variables.x_ip,
        x_port=cgn_variables.x_port,
        dst_ip=cgn_variables.dst_ip,
        dst_port=cgn_variables.dst_port,
    )

    assert mapping.timestamp == now
    assert IPv4Interface(mapping.host).ip == cgn_variables.host
    assert mapping.vrf_id == cgn_variables.vrf_id
    assert mapping.protocol == cgn_variables.protocol
    assert IPv4Interface(mapping.src_ip).ip == cgn_variables.src_ip
    assert mapping.src_port == cgn_variables.src_port
    assert IPv4Interface(mapping.x_ip).ip == cgn_variables.x_ip
    assert mapping.x_port == cgn_variables.x_port
    assert IPv4Interface(mapping.dst_ip).ip == cgn_variables.dst_ip
    assert mapping.dst_port == cgn_variables.dst_port
