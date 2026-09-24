# Copyright (C) 2026 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

"""Hop 4 of 6 - routes the streaming response to the right buffer."""

from payload_buffer import PayloadBuffer


class ResponseRouter:
    def __init__(self) -> None:
        self._buffer = PayloadBuffer()

    def route(self, response) -> str:
        if response is None:
            return ""
        return self._buffer.collect(response)
