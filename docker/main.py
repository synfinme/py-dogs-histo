#!/usr/bin/env python3

import datadog
import os
import random
import sys
import time

try:
    from dataset import data
except ImportError:
    from default_dataset import data


METRIC_NAME_SUFFIX = os.environ.get('METRIC_NAME_SUFFIX', '')
STATSD_HOST        = os.environ.get('DD_AGENT_HOST', '127.0.0.1')
STATSD_PORT        = os.environ.get('DD_DOGSTATSD_PORT', '8125')
DELAY_SECONDS      = os.environ.get('DELAY_SECONDS', '0.1')

metric_name = 'py_dogstatsd_histo'
if len(METRIC_NAME_SUFFIX) > 0:
    metric_name += '_' + METRIC_NAME_SUFFIX


def init():
    options = {
        'statsd_host': STATSD_HOST,
        'statsd_port': int(STATSD_PORT)
    }
    print('init(): options =', options)
    datadog.initialize(**options)


def update_stats():
    # Streams dataset into DD Agent (DatadogStatsD)
    for v in data:
        datadog.statsd.histogram(metric_name, v)
        time.sleep(float(DELAY_SECONDS))


def main():
    init()

    x = 0
    while True:
        update_stats()
        x += 1

        # Some cosmetic stuff
        sys.stdout.write('.')
        sys.stdout.flush()
        if (x % 60) == 59:
            sys.stdout.write('\n')
            sys.stdout.flush()


if __name__ == '__main__':
    main()
