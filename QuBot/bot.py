import discord
import time

async def PIR_1():
    fr = open("signal.txt", 'r')
    if fr.read() == "1":
        user = client.get_user(110053345636405248)
        await user.send('hello')
    fr.close()

    time.sleep(5)

    await PIR_1()


class MyClient(discord.Client):
    async def on_ready(self):
        print("ready")

        await PIR_1()


client = MyClient()

client.run("NDgzNDAwMzM2MDU3NTY1MTg1.XMxZtQ.JFl2CxolUSkd0L7gzQZmriTsiZY")

