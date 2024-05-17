import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba ben {bot.user}! Ben çevre dostu bir botum!')
    time.sleep(1)
    await ctx.send(f'Ben nereye cöp atmaniza yardim ederim!')
    time.sleep(1)
    await ctx.send(f'Komutlar: .ambalaj, .atik_cam, .atik_pet_sise, .atik_pil, .tutorial, .satin_almak ve .cocuk_oyun')


@bot.command()
async def ambalaj(ctx):
    await ctx.send(f'Kağıt, Karton, plastik, metal, kompozit atıklarınızı mavi renkli Ambalaj Atık Kutularına atabilir, binlerce ağaç kurtarabilir, tonlarca petrol tasarruf edebilirsiniz.')
    time.sleep(1)
    with open(r"Ders6\resimler\Ambalaj.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def atik_cam(ctx):
    await ctx.send(f'Cam şişe ve kavanozlarınızı yeşil-beyaz renkli Cam Kumbaralarına atabilir, çevreyi korurken enerji tasarrufu sağlayabilirsiniz. Bir cam şişe doğada 4000 yıl yok olmadan kalabilir. Cam kalitesinden hiçbir şey kaybetmeden %100 geri dönüşür.')
    time.sleep(1)
    with open(r"Ders6\resimler\org_pxdnxc4e.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def atik_pet_sise(ctx):
    await ctx.send(f'Tüm atık pet şişelerinizi pet şişe şeklindeki Pet Şişe Kumbaralarına atabilirsiniz. Denizlerimiz, göllerimiz, topraklarımız plastik ile kirleniyor. Canlılar plastik yiyor. Plastik kullanımını azaltarak doğal kaynaklarımızı koruyabilir, enerji tasarrufu sağlayabilir ve canlılarımızı kurtarabilirsiniz.')
    time.sleep(1)
    with open(r"Ders6\resimler\pet.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def atik_pil(ctx):
    await ctx.send(f'Bütün atık pillerinizi okullar, muhtarlıklar, kamu kurumları ve bazı marketlerde bulunan kırmızı renkli Atık Pil Kutularına atabilirsiniz. Bir kalem pil 4 m3 toprağı ve 800.000 lt suyu kirletir.')
    time.sleep(1)
    with open(r"Ders6\resimler\pil.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def tutorial(ctx):
    youtube = "https://www.youtube.com/watch?v=kqjS6vW9BZQ"
    await ctx.send(f'Daha fazla bilgi almak isterseniz linke basiniz --> {youtube}')

@bot.command()
async def satin_almak(ctx):
    shop = "https://www.hijyenmarket.net/sifir-atik-geri-donusum-cop-kovasi-cember-kapakli-boyali-paslanmaz-65"
    await ctx.send(f'Geridönüsum kutusunu satin almak icin bu linke basiniz --> {shop}')

@bot.command()
async def cocuk_oyun(ctx):
    oyun = "https://sifiratiktema.org/oyna-ogren/bantoyunu/"
    await ctx.send(f'Cocuklariniza geridonusumu ogretmek icin bir oyun --> {oyun}')

bot.run("token")
