from time import sleep

from userbot import CMD_HELP
from userbot.events import register






# Create by myself @localheart


@register(outgoing=True, pattern="^.kcg(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "`Hi kawan`"







    )
    sleep(1)
    await typew.edit(
        "`\nKacang...`"
 

    )
    sleep(2)
    await typew.edit(
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n**Aku Nyimak Ajalah**"
    )


@register(outgoing=True, pattern="^.punten(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n**Punten**"
    )


@register(outgoing=True, pattern="^.pantau(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n**Masih Ku Pantau**"
    )


# Create by myself @localheart

CMD_HELP.update(
    {
        "animasi2": "`.kcg`\
    \nUsage: bot.\
    \n\n`.punten` ; `.pantau`\
    \nUsage: liat aja.\



    


    }
)
