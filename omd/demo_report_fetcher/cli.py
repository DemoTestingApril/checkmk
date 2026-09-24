# Copyright (C) 2026 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

"""Hop 1 of 6 - command line entry point for the report fetcher."""

import argparse

from report_client import ReportClient


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch a remote inventory report")
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    client = ReportClient()
    print(client.fetch_report(args.url))


if __name__ == "__main__":
    main()
