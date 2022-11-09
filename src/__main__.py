import argparse

from . import __version__

parser = argparse.ArgumentParser(__file__)
parser.add_argument('--version', action='version',
                    version=f'%(prog)s {__version__}')
parser.add_argument('--async', action='store_true', dest='async_')
parser.add_argument('url')

args = parser.parse_args()

print('Command-line arguments:', args)

if args.async_:
    import asyncio

    import aiohttp

    async def main():
        async with aiohttp.ClientSession() as session:
            print(await (await session.get(args.url)).text())

    asyncio.run(main())
else:
    import requests

    with requests.Session() as session:
        print(session.get(args.url).text)
