# Async Client
async def send_file_async(filename, host='localhost', port=5000):
    reader, writer = await asyncio.open_connection(host, port)
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            writer.write(data)
            await writer.drain()
    writer.close()
    await writer.wait_closed()
    print("File sent")
