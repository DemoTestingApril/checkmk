# Copyright (C) 2026 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

"""Hop 2 of 6 - client facade over the HTTP transport."""

from http_transport import HttpTransport
from response_router import ResponseRouter


class ReportClient:
    def __init__(self) -> None:
        self._transport = HttpTransport()
        self._router = ResponseRouter()

    def fetch_report(self, url: str) -> str:
        response = self._transport.open_stream(url)
        return self._router.route(response)
