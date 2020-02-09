# B.A.N Police

2.3.20: This is a side project for the encouraged automation of the Google IT Automation Python Professional Certificate.  I plan on this to be a discord bot that when running will continuously send a selected user to the afk channel in my discord server if they are not in it.

2.3.20: Lots of old guides outdated.  Among them send_message being outdated and mostly replaced by message.channel.send or user.send.  Fuckloads of events to play with.  Getting a specific user id to send private messages was very straight- forward.  In fact everything seems pretty straight-forward so far.  I hope there is a event to detect a specific user id entering specific channel ids.  Pycharm is godlike I don't know why I haven't tried this before.

2.8.20: Oh, so on_voice_state_update literally looks like it can track when a member joins a voice channel.  Very useful, much better than other hacky ideas I had.

2.8.20: Starting to get a better feel for the properties.  Stuff like assuming that messages.guild.afk_channel was a thing based on how the other syntax worked.  Pretty intuitive api tbh.

2.8.20: I suddenly realize how troublesome it would be to make something like pokecord.  I currently cannot fathom how I would handle that many requests.