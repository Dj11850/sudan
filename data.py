import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NjM0MjQ3NDg2NzM4OTIzNTMw.XarVnw.PEehU4ESSKmsYFuvcKD1USUZOR0'
self_bot_token = 'NTY5OTE4NzExMDcxNTA2NDYz.XWE1fg.YjRvlGfCdAma7nUs7rt2Zkf-isk '

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '633545594111000588')

input_hq_private  = [
    "595300313930530833",
    "459842150323060736",
    "580198028950896640",
	    "513818250652680213",
	    "595639586726740049",
	    "568617830258442255",
	    "569420198717816852",
	    "591600008353021953",
	    "585285701671714826",
	    "595301050374815757",
	    "590471026899550208",
	    "589120764347678750",
	    "585682137202819101",
	    "590470896649502750",
	    "590182635653824542",
	    "589120764347678750",
	    "589516793350062100",
    "583796470394781696",
    "569420128794443776",   answers1
    "571681709926645770", #answers2
    '633545594111000588' #trivia-answers
]
input_hq_public = ['633545594111000588']
command_channel = '633545594111000588' #trivia-answers
admin_chat = '633545594111000588' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
