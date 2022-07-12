import os
import random
import time
from deep_fried_meme import deep_frier
from textwrap import wrap

import cv2
import discord
import numpy as np
import requests
import wolframalpha
from PIL import Image, ImageDraw, ImageFont
from discord.ext import commands
from google_images_search import GoogleImagesSearch

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)


@bot.command()  # imitates a coinflip
async def flip(ctx):
    coin = random.randint(1, 10)
    if coin <= 5:
        await ctx.send("*ОРЕЛ*")
    else:
        await ctx.send("*РЕШКА*")


wolframalpha_client_id = open('C://Users//Max//Desktop//pyth//wolframalpha_client.txt', 'r')
client = wolframalpha.Client(wolframalpha_client_id.read())


@bot.command()  # basic wolframalpha calculator
async def calc(ctx):
    request = str(ctx.message.content[6:len(ctx.message.content)])
    result = client.query(request)
    output = next(result.results).text
    await ctx.send(output)


@bot.command()  # more complex calculator function for many variables
async def kalk(ctx):
    request = str(ctx.message.content[6:len(ctx.message.content)])
    result = client.query(request)
    # output=res.results
    p = str(result)
    answer = set()
    while p.count("@alt': 'x =") > 0:
        start = p.find("@alt': 'x =")
        fin = p.find("', '@title': 'x =")
        returned_variable = p[start + 8:fin]
        print(returned_variable)
        answer_length = len(p)
        p = p[fin + 8:answer_length]
        answer.add(returned_variable)
    print(answer)
    for i in answer:
        await ctx.send(i)


@bot.command()  # returns input from console do discord chat
async def ask_a_god(ctx):
    print((ctx.message.content)[11:len(ctx.message.content)])
    await ctx.send(input())


@bot.command()  # enlarges text with emojis
async def big(ctx):
    input_tekst = ctx.message.content
    smol_input = input_tekst[5:len(input_tekst)]
    big_string = str()
    for i in range(len(smol_input)):
        if smol_input[i] != ' ':
            bukva = smol_input[i]
            big_string += ":regional_indicator_" + bukva + ": "
        else:
            big_string += " "
    await ctx.send(big_string)


@bot.command()  # basic ping function
async def vibecheck(ctx):
    await ctx.send("Yes, honey")


@bot.command()  # hello function with mention
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello {author.mention}")


@bot.command()  # return picture as an attachment to a message
async def vsem(ctx):
    await ctx.send(file=discord.File('vsem.jpg'))


@bot.command()  # returns inputted text
async def text(ctx):
    TEXT = ctx.message.content
    reg = TEXT[6:len(TEXT)]
    await ctx.send(reg)


@bot.command()  # modified coinflip with file attachment
async def base(ctx):
    perem = random.randint(1, 10)
    if perem % 2 == 0:
        await ctx.send(file=discord.File('C://Users//Max//Desktop//pyth//based.png'))
    else:
        await ctx.send(file=discord.File('C://Users//Max//Desktop//pyth//cringe.png'))


@bot.command()  # in regards to R.Gorkovets
async def где(ctx):
    await ctx.send("Лофт")

list_of_files_one = []
list_of_files_two = []


def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        list_of_files_one.append(fileName)


FOLDER_PATH = r"C:\Users\Max\Desktop\pyth\images"


def listDir1(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        if fileName in list_of_files_one:
            print("exists")
        else:
            list_of_files_two.append(os.path.abspath(os.path.join(dir, fileName)))
            print(fileName)


@bot.command()
async def google(ctx):  # returns a first found picture by a request
    TEXT = ctx.message.content
    req = TEXT[7:(len(TEXT))]
    gis = GoogleImagesSearch("AIzaSyBuceSxeAoGGjYZIqxoVR_G6YHngXlzxes", "002797577232917170979:zd6ar5n6hhj")
    listDir(FOLDER_PATH)
    _search_params = {
        'q': req,
        'num': 1,
    }
    gis.search(search_params=_search_params)
    for image in gis.results():
        image.download(r"C:\Users\Max\Desktop\pyth\images")
    after = ""
    listDir1(FOLDER_PATH)
    await ctx.send(file=discord.File(list_of_files_two[0]))
    print(list_of_files_two)
    os.remove(list_of_files_two[0])
    del list_of_files_two[0]
    print(list_of_files_two)


@bot.command()  # returns one of first 10 pictures by request
async def gorand(ctx):
    number = random.randint(1, 10)
    TEXT = ctx.message.content
    request = TEXT[7:(len(TEXT))]
    counter = 0
    gis = GoogleImagesSearch("AIzaSyBuceSxeAoGGjYZIqxoVR_G6YHngXlzxes", "002797577232917170979:zd6ar5n6hhj")
    listDir(FOLDER_PATH)
    _search_params = {
        'q': request,
        'num': 10,
        'fileType': 'jpg,png,gif'
    }
    gis.search(search_params=_search_params)
    for image in gis.results():
        counter += 1
        if counter != number:
            counter = counter
        else:
            image.download(r"C:\Users\Max\Desktop\pyth\images")

    after = ""
    listDir1(FOLDER_PATH)
    print(list_of_files_two)
    await ctx.send(file=discord.File(list_of_files_two[0]))
    os.remove(list_of_files_two[0])
    del list_of_files_two[0]
    time.sleep(5)


@bot.command()
async def roll(ctx, bottom_number, top_number):  # returns a random number in a segment
    await ctx.send(random.randint(int(bottom_number), int(top_number)))


@bot.command()
async def deepfry(ctx):  # picture frier
    deepfry_input = ctx.message.attachments
    deepfry_rawurl = str(deepfry_input)
    deepfry_url_start = deepfry_rawurl.find('url=') + 5
    deepfry_url_end = -3
    deepfry_url = deepfry_rawurl[deepfry_url_start:deepfry_url_end]
    r = requests.get(deepfry_url)
    with open("deepfry_sent.png", 'wb') as outfile:
        outfile.write(r.content)
    print(deep_frier('deepfry_sent.png', config=None, putout_scheme=['file', 'deepfry_return', 'jpg']))
    await ctx.send(file=discord.File("deepfry_return.jpg"))


@bot.command()
async def dem(ctx):  # returns a default demotivator with sent picture
    # sent_pic=await ctx.to_file()
    await ctx.send("send pic")
    sent_picture = ((await bot.wait_for('message')).attachments)
    print(sent_picture)
    unitedrl = str(sent_picture)
    start = unitedrl.find("url=") + 5
    end = -3
    url = unitedrl[start:end]
    # url1=ctx.message.attachments[0]['proxy_url']
    # print(url1)
    print(url)
    r = requests.get(url)
    with open("what_you_sent.png", 'wb') as outfile:
        outfile.write(r.content)
    image = Image.open("C://Users//Max//Desktop//pyth//testpic.jpg").convert("RGBA")
    width, height = image.size
    imagepaste = Image.open("what_you_sent.png").convert("RGBA")
    # imagefinale=Image.new("RGBA", (width+50,height+50), (0,0,0,0))
    imagepaste1 = imagepaste.resize((505, 501))
    image.paste(imagepaste1, (56, 56))
    image.save("demot.png")
    await ctx.send(file=discord.File("demot.png"))
    # urllib.request.urlretrieve(url, 'what_you_sent.png')
    # print(ctx.attachment.filename)


def font_size(line):
    a = len(line)
    if a <= 13:
        return 100
    if 14 <= a <= 15:
        return 88
    if 16 <= a <= 17:
        return 80
    if 18 <= a <= 19:
        return 70
    if 20 <= a <= 21:
        return 62
    if 22 <= a <= 23:
        return 55
    if 24 <= a <= 28:
        return 48
    if 29 <= a <= 34:
        return 40
    if 35 <= a <= 41:
        return 31
    if 42 <= a <= 55:
        return 23
    if 56 <= a:
        return 16


@bot.command()
async def demot(ctx):  # return a demotivator with a custom text
    raw_line = ctx.message.content[7:len(ctx.message.content)]
    await ctx.send("send picture")
    sent_picture = ((await bot.wait_for('message')).attachments)
    url_raw = str(sent_picture)
    START = url_raw.find("url=") + 5
    END = -3
    url = url_raw[START:END]
    r = requests.get(url)
    with open("sent_picture.png", 'wb') as outfile:
        outfile.write(r.content)
    empty = Image.open('empty_template.jpg').convert("RGBA")
    WIDTH, HEIGHT = empty.size
    image_to_paste = Image.open("sent_picture.png").convert("RGBA")
    image_to_paste_one = image_to_paste.resize((569, 503))
    empty.paste(image_to_paste_one, (54, 54))
    empty.save("middle.png")
    if len(raw_line) > 80:
        line = '\n'.join(wrap(raw_line, width=80))
    else:
        line = raw_line
    middle = Image.open("middle.png")
    draw = ImageDraw.Draw(middle)
    size = font_size(line)
    font = ImageFont.truetype("Times New Roman.ttf", size)
    w, h = draw.textsize(line, font=font)
    draw.multiline_text(((WIDTH - w) // 2, 597), line, (255, 255, 255), font=font, align='center')
    middle.save("demot_to_sent.png")
    await ctx.send(file=discord.File("demot_to_sent.png"))


@bot.command()
async def fisheye(ctx):  # applies a rough fisheye effect to a sent picture
    fisheye_input = ctx.message.attachments
    fisheye_rawurl = str(fisheye_input)
    fisheye_url_start = fisheye_rawurl.find('url=') + 5
    fisheye_url_end = -3
    fisheye_url = fisheye_rawurl[fisheye_url_start:fisheye_url_end]
    r = requests.get(fisheye_url)
    with open("fisheye_sent.png", 'wb') as outfile:
        outfile.write(r.content)
    src = cv2.imread('fisheye_sent.png')
    h, w = src.shape[0:2]
    # высота и ширина изображения
    print(h, w)

    # заполняем матрицу преобразования. сначала все нулями
    intrinsics = np.zeros((3, 3), np.float64)

    # матрица intrinsics
    intrinsics[0, 0] = 3500
    intrinsics[1, 1] = 3500
    intrinsics[2, 2] = 1.0
    intrinsics[0, 2] = w / 2.
    intrinsics[1, 2] = h / 2.
    print(intrinsics)

    newCamMtx = np.zeros((3, 3), np.float64)
    newCamMtx[0, 0] = 3500
    newCamMtx[1, 1] = 3500
    newCamMtx[2, 2] = 1.0
    newCamMtx[0, 2] = w / 2.
    newCamMtx[1, 2] = h / 2.

    dist_coeffs = np.zeros((1, 4), np.float64)
    dist_coeffs[0, 0] = -40.0
    dist_coeffs[0, 1] = 0.0
    dist_coeffs[0, 2] = 0.0
    dist_coeffs[0, 3] = -0.0
    print(dist_coeffs)

    map1, map2 = cv2.initUndistortRectifyMap(intrinsics, dist_coeffs, None, newCamMtx, src.shape[:2], cv2.CV_16SC2)
    res = cv2.remap(src, map1, map2, cv2.INTER_LINEAR)

    # path = "C:\Users\Max\Desktop\pyth"
    # cv2.imshow("Image_res", res)
    # cv2.imshow("Image_origin", src)
    cv2.imwrite(r'fisheye_new.jpg', res)
    cv2.waitKey(0)
    await ctx.send(file=discord.File("fisheye_new.jpg"))


@bot.command()
async def cursed(ctx):  # gif saving demotivator with no text
    raw_line = ctx.message.content[8:len(ctx.message.content)]
    await ctx.send("send picture")
    sent_picture = ((await bot.wait_for('message')).attachments)
    url_raw = str(sent_picture)
    START = url_raw.find("url=") + 5
    END = -3
    url = url_raw[START:END]
    r = requests.get(url)
    with open("sent_picture.gif", 'wb') as outfile:
        outfile.write(r.content)
    empty = Image.open('empty_template.jpg').convert("RGBA")
    WIDTH, HEIGHT = empty.size
    image_to_paste = Image.open("sent_picture.gif").convert("RGBA")
    image_to_paste_one = image_to_paste.resize((569, 503))
    empty.paste(image_to_paste_one, (54, 54))
    empty.save("middle.gif")
    if len(raw_line) > 80:
        line = '\n'.join(wrap(raw_line, width=80))
    else:
        line = raw_line
    middle = Image.open("middle.gif")
    draw = ImageDraw.Draw(middle)
    size = font_size(line)
    font = ImageFont.truetype("Times New Roman.ttf", int(size))
    w, h = draw.textsize(line, font=font)
    draw.multiline_text(((WIDTH - w) // 2, 597), line, (255, 255, 255), font=font, align='center')
    middle.save("cursed_end.gif")
    await ctx.send(file=discord.File("cursed_end.gif"))


@bot.command()
async def zhim(ctx):  # quality lowering function for a picture
    sent_picture = ctx.message.attachments
    url_raw = str(sent_picture)
    START = url_raw.find("url=") + 5
    END = -3
    url = url_raw[START:END]
    r = requests.get(url)
    with open("sent_picture.jpg", 'wb') as outfile:
        outfile.write(r.content)
    im1 = Image.open("sent_picture.jpg")
    IMAGE_10 = os.path.join('Shakal.jpeg')
    try:
        im1.save(IMAGE_10, "JPEG", quality=1)
        await ctx.send(file=discord.File("Shakal.jpeg"))
    except:
        await ctx.send("Только '.jpg' файлы!")


def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != "...":
            winner = board[row[0]]
            return winner

    if "..." not in board:
        return "TIE"

    return None


@bot.command()
async def xo(ctx):  # Tic-Tac-Toe game
    X = "X"
    O = "O"
    NUM_SQUARES = 9
    await ctx.send("Welcome to the second greatest intellectual challenge of all time: Tic-Tac-Toe.\nThis will be a "
                   "showdown between a human brain and silicon processor.\n\nMake your move by entering a number, "
                   "0-8. The number will correspond to the board position as shown.")
    await ctx.send(file=discord.File("game_beginn.png"))
    await ctx.send("Do you require the first move? (y/n): ")
    go_first = (await bot.wait_for('message')).content
    if go_first == "y":
        await ctx.send("\nThen take the first move.  You will need it.")
        human = X
        computer = O
    else:
        await ctx.send("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    turn = X
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append("...")
    image = Image.new("RGBA", (300, 300), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 300, 300), fill="black")
    draw.line((100, 0, 100, 300), fill="white")
    draw.line((200, 0, 200, 300), fill="white")
    draw.line((0, 100, 300, 100), fill="white")
    draw.line((0, 200, 300, 200), fill="white")
    font = ImageFont.truetype("C:/Users/Max/Desktop/pyth/Times New Roman.ttf", 32)
    d = ImageDraw.Draw(image)
    d.text((40, 33), "0", font=font, fill=(255, 255, 255, 128))
    d.text((143, 33), "1", font=font, fill=(255, 255, 255, 128))
    d.text((240, 33), "2", font=font, fill=(255, 255, 255, 128))
    d.text((40, 133), "3", font=font, fill=(255, 255, 255, 128))
    d.text((143, 133), "4", font=font, fill=(255, 255, 255, 128))
    d.text((240, 133), "5", font=font, fill=(255, 255, 255, 128))
    d.text((40, 233), "6", font=font, fill=(255, 255, 255, 128))
    d.text((143, 233), "7", font=font, fill=(255, 255, 255, 128))
    d.text((240, 233), "8", font=font, fill=(255, 255, 255, 128))
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    await ctx.send(file=discord.File('C:/Users/Max/Desktop/pyth/game_begin.png'))
    while not winner(board):
        moves = []
        for square in range(NUM_SQUARES):
            if board[square] == "...":
                moves.append(square)
        if turn == human:
            move = None
            while move not in moves:
                await ctx.send("Where will you move? (0 - 8):")
                response = None
                while response not in range(0, NUM_SQUARES):
                    response = (int((await bot.wait_for('message')).content))
                    if response not in moves:
                        await ctx.send("That square is already occupied, foolish human. Choose another")
                move = response
            await ctx.send("Fine")
            board[move] = human
            moves.remove(move)
            if human == "X":
                if move == 0:
                    x = 50
                    y = 50
                if move == 1:
                    x = 150
                    y = 50
                if move == 2:
                    x = 250
                    y = 50
                if move == 3:
                    x = 50
                    y = 150
                if move == 4:
                    x = 150
                    y = 150
                if move == 5:
                    x = 250
                    y = 150
                if move == 6:
                    x = 50
                    y = 250
                if move == 7:
                    x = 150
                    y = 250
                if move == 8:
                    x = 250
                    y = 250
                x2 = x + 50
                y2 = y + 50
                x3 = x - 50
                y3 = y - 50
                draw.line((x3, y2, x2, y3), fill="white")
                draw.line((x3, y3, x2, y2), fill="white")
            else:
                if move == 0:
                    x = 50
                    y = 50
                if move == 1:
                    x = 150
                    y = 50
                if move == 2:
                    x = 250
                    y = 50
                if move == 3:
                    x = 50
                    y = 150
                if move == 4:
                    x = 150
                    y = 150
                if move == 5:
                    x = 250
                    y = 150
                if move == 6:
                    x = 50
                    y = 250
                if move == 7:
                    x = 150
                    y = 250
                if move == 8:
                    x = 250
                    y = 250
                x2 = x + 50
                y2 = y + 50
                x3 = x - 50
                y3 = y - 50
                draw.ellipse((x3, y3, x2, y2), width=2, outline="white")
        else:
            board1 = board[:]
            checkmate = 0
            humanmate = 0
            for move in moves:
                board1[move] = computer
                if (board1[0] == board1[1] == board1[2] == computer) or (
                        board1[3] == board1[4] == board1[5] == computer) or (
                        board1[6] == board1[7] == board1[8] == computer) or (
                        board1[0] == board1[3] == board1[6] == computer) or (
                        board1[1] == board1[4] == board1[7] == computer) or (
                        board1[2] == board1[5] == board1[8] == computer) or (
                        board1[0] == board1[4] == board1[8] == computer) or (
                        board1[2] == board1[4] == board1[6] == computer):
                    move = move
                    checkmate = 1
                    break
                board1[move] = "..."
            if checkmate == 0:
                for move in moves:
                    board1[move] = human
                    if (board1[0] == board1[1] == board1[2] == human) or (
                            board1[3] == board1[4] == board1[5] == human) or (
                            board1[6] == board1[7] == board1[8] == human) or (
                            board1[0] == board1[3] == board1[6] == human) or (
                            board1[1] == board1[4] == board1[7] == human) or (
                            board1[2] == board1[5] == board1[8] == human) or (
                            board1[0] == board1[4] == board1[8] == human) or (
                            board1[2] == board1[4] == board1[6] == human):
                        move = move
                        humanmate = 1
                        break
                    board1[move] = "..."
                if humanmate == 0:
                    for move in BEST_MOVES:
                        if move in moves:
                            move = move
                            break
            moves.remove(move)
            board[move] = computer
            if computer == "X":
                if move == 0:
                    x = 50
                    y = 50
                if move == 1:
                    x = 150
                    y = 50
                if move == 2:
                    x = 250
                    y = 50
                if move == 3:
                    x = 50
                    y = 150
                if move == 4:
                    x = 150
                    y = 150
                if move == 5:
                    x = 250
                    y = 150
                if move == 6:
                    x = 50
                    y = 250
                if move == 7:
                    x = 150
                    y = 250
                if move == 8:
                    x = 250
                    y = 250
                x2 = x + 50
                y2 = y + 50
                x3 = x - 50
                y3 = y - 50
                draw.line((x3, y2, x2, y3), fill="white")
                draw.line((x3, y3, x2, y2), fill="white")
            else:
                if move == 0:
                    x = 50
                    y = 50
                if move == 1:
                    x = 150
                    y = 50
                if move == 2:
                    x = 250
                    y = 50
                if move == 3:
                    x = 50
                    y = 150
                if move == 4:
                    x = 150
                    y = 150
                if move == 5:
                    x = 250
                    y = 150
                if move == 6:
                    x = 50
                    y = 250
                if move == 7:
                    x = 150
                    y = 250
                if move == 8:
                    x = 250
                    y = 250
                x2 = x + 50
                y2 = y + 50
                x3 = x - 50
                y3 = y - 50
                draw.ellipse((x3, y3, x2, y2), width=2, outline="white")
            await ctx.send("I shall take the number...")
            await ctx.send(str(move))
            board[move] = computer
        # saving pil image and sending it
        image.save("finale.png")
        await ctx.send(file=discord.File('finale.png'))
        if turn == X:
            turn = O
        else:
            turn = X
    the_winner = winner(board)
    if the_winner == computer:
        await ctx.send("As I predicted, human, I am triumphant once more. Proof that computers are superior to humans "
                       "in all regards.")
    elif the_winner == human:
        await ctx.send(
            "No, no!  It cannot be! Somehow you tricked me, human. But never again! I, the computer, so swear it!")
    elif the_winner == "TIE":
        await ctx.send("You were most lucky, human, and somehow managed to tie me. Celebrate today... for this is the "
                       "best you will ever achieve.")


@bot.command()  # throws a random peaky blinders gif
async def shelby(ctx):
    gif_number = random.randint(1, 77)
    full_path = os.path.abspath('main.py')
    await ctx.send(file=discord.File(f"{full_path[0:38]}\shelby\shelby ({gif_number}).gif"))


bot_token = open('C://Users//Max//Desktop//pyth//token.txt', 'r')
bot.run(bot_token.read())
