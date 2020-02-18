# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

import pytest
from datadog_checks.base import ConfigurationError

from datadog_checks.pgbouncer import PgBouncer


@pytest.mark.unit
def test_critical_service_check(instance, aggregator):
    check = PgBouncer('pgbouncer', {}, [instance])
    try:
        check.check(instance)
    except Exception:
        pass
    aggregator.assert_service_check(PgBouncer.SERVICE_CHECK_NAME, status=PgBouncer.CRITICAL)


@pytest.mark.unit
def test_config_missing_host(instance):
    with pytest.raises(ConfigurationError):
        del instance['host']
        PgBouncer('pgbouncer', {}, [instance])


@pytest.mark.unit
def test_config_missing_user(instance):
    with pytest.raises(ConfigurationError):
        del instance['username']
        PgBouncer('pgbouncer', {}, [instance])
