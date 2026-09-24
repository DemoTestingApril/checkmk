# Copyright (C) 2026 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

"""Hop 5 of 6 - buffers the response before decoding."""

from stream_decoder import StreamDecoder


class PayloadBuffer:
    def __init__(self) -> None:
        self._decoder = StreamDecoder()

    def collect(self, response) -> str:
        return self._decoder.decode(response)
