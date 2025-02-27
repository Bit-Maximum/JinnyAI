from discord.ext import commands
import discord
import asyncio

from src.config.cogs import default_params


class NotInVCException(Exception):
    pass


class Voice(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.vc = None

    def _check_connection(self) -> bool:
        return self.vc is not None and self.vc.is_connected()

    async def _disconnect(self) -> bool:
        if self._check_connection():
            await self.vc.disconnect()
            return True
        return False

    @discord.slash_command(description="Join a voice channel", **default_params)
    @discord.option(
        name="channel",
        type=discord.VoiceChannel,
        description="The voice channel to join",
    )
    async def join_vc(self, ctx, channel: discord.VoiceChannel) -> None:
        try:
            await self._disconnect()  # disconnect from current voice channel if any
            self.vc = await channel.connect()
            await ctx.respond(content=f"Joined {channel}")
        except discord.ClientException as err:
            print(err)
            await ctx.respond(
                content=f"Failed to change channel to {channel}. Try again..."
            )
            return
        except asyncio.TimeoutError as err:
            print(err)
            await ctx.respond(content=f"Timeout to join {channel}. Try again...")
            return
        except Exception as err:
            print(err)
            await ctx.respond(content=f"Failed to join {channel}...")
            return

    @discord.slash_command(description="Leave current voice channel", **default_params)
    async def leave_vc(self, ctx) -> None:
        try:
            if not await self._disconnect():
                raise NotInVCException()
            else:
                await ctx.respond(f"Left voice channel")
        except NotInVCException as err:
            print(err)
            await ctx.respond(f"Not in a voice channel")
            return
        except Exception as err:
            print(err)
            await ctx.respond(f"Error during leaving voice channel")
            return

    @discord.slash_command(description="Play a sound", **default_params)
    async def play_sound(self, ctx) -> None:
        try:
            if not self._check_connection():
                raise NotInVCException()
            source = discord.FFmpegPCMAudio(
                "G:\\Projects\\Python\\JinnyAI\\assets\\sfx\\rock.ogg"
            )
            self.vc.play(source, wait_finish=True)
            await ctx.respond(
                content=f"Played sound in channel '{self.vc.channel.name}'"
            )
        except NotInVCException as err:
            print(err)
            await ctx.respond(
                f"Not in a voice channel. You need to join the voice channel first."
            )
            return
        except Exception as err:
            print(err)
            await ctx.respond(f"Error during playing sound")
            return

    async def _record_callback(self, sink: discord.sinks) -> None:
        raw_audio = sink.get_all_audio()
        for buffer in range(len(raw_audio)):
            with open(f"recordings/{buffer}.mp3", "wb") as f:
                f.write(raw_audio[buffer].getbuffer())

    @discord.slash_command(
        description="Start recording audio from users in current voice chanel",
        **default_params,
    )
    async def start_recording(self, ctx) -> None:
        try:
            if not self._check_connection():
                raise NotInVCException()
            sink = discord.sinks.MP3Sink()
            self.vc.start_recording(sink, self._record_callback, sync_start=True)
            await ctx.respond(f"Started recording")
        except NotInVCException as err:
            print(err)
            await ctx.respond(f"Not in a voice channel")
            return
        except discord.sinks.RecordingException as err:
            print(err)
            await ctx.respond(f"Already recording")
            return
        except Exception as err:
            print(err)
            await ctx.respond(f"Failed to start recording")
            return

    @discord.slash_command(description="Stop recording", **default_params)
    async def stop_recording(self, ctx) -> None:
        try:
            if not self._check_connection():
                raise NotInVCException()
            self.vc.stop_recording()
            await ctx.respond(f"Stopped recording")
        except NotInVCException as err:
            print(err)
            await ctx.respond(f"Not in a voice channel")
        except discord.sinks.RecordingException as err:
            print(err)
            await ctx.respond(f"Was not even recording")
        except Exception as err:
            print(err)
            await ctx.respond(f"Failed to stop recording")
            return


def setup(bot: discord.Bot) -> None:
    """Augment inputted bot with this cog"""
    bot.add_cog(Voice(bot))
