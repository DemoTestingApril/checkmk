# Copyright (C) 2026 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

"""Hop 6 of 6 - taint sink for CVE-2025-66471.

Reading the lazily loaded body here performs the vulnerable decode.
"""


class StreamDecoder:
    def decode(self, response) -> str:
        raw = response.read()
        return raw.decode("utf-8", errors="replace")
