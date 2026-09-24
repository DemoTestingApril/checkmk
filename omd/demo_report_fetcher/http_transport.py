# Copyright (C) 2026 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

"""Hop 3 of 6 - opens the streaming HTTP response.

The urllib3 request below is the taint source for CVE-2025-66471: the
response is requested with `preload_content=False`, so the body is decoded
lazily downstream.
"""

import urllib3


class HttpTransport:
    def open_stream(self, url: str):
        return urllib3.PoolManager().request("GET", url, preload_content=False)
