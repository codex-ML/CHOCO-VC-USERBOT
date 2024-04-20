


@app.on_message(filters.regex('.resume'))
async def resume_handler(_: Client, message: Message):
  await message.reply_text(text="Userbot  resume song")
  await pytg.resume_stream(message.chat.id, )
