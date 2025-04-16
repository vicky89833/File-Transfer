# Async Server
import asyncio

async def handle_client(reader, writer):
    data = await reader.read(1024)
    with open('received_file', 'wb') as f:
        while data:
            f.write(data)
            data = await reader.read(1024)
    print("File received")
    writer.close()

async def start_async_server(host='0.0.0.0', port=5000):
    server = await asyncio.start_server(handle_client, host, port)
    async with server:
        await server.serve_forever()
