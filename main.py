import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def itadori(ctx):
    await ctx.send("He is main character of Jujutsu Kaisen, he is a good guy but he is not strong enough to beat me ;)") 
@bot.command()
async def carp(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)
@bot.command()
async def sukuna(ctx):
    await ctx.send("Sukuna is a powerful cursed spirit in Jujutsu Kaisen, but he is not as strong as me. I am the strongest.")
@bot.command()
async def gojo(ctx):
    await ctx.send("Im there strongest sorcerer in Jujutsu Kaisen, but even I have my limits. I can defeat any cursed spirit, but I cannot defeat myself. I am the strongest, but I am also the weakest.")
@bot.command()
async def sukuna_better(ctx):
    await ctx.send("Imaginary Technique: Red  Imaginary Technique:Blue  Imaginary Technique: Hollow Purple go and cry lil bro ")
@bot.command()
async def bolme(ctx, left: int, right: int):
    """Divides two numbers."""
    if right == 0:
        await ctx.send("Sıfıra bölme hatası!")
    else:
        await ctx.send(left / right)
@bot.command()
async def tekrarla(ctx, *, message: str):
    """Tekrarla komutu ile istediğiniz mesajı tekrar edebilirsiniz."""
    await ctx.send(message)
@bot.command()
async def domain_expansion(ctx):
    await ctx.send("Domain Expansion: Infinite Void!")

@bot.command()
async def death_note(ctx):
    await ctx.send("Bro thats a PEAK anime, but I am not a fan of it. I prefer Jujutsu Kaisen. But I can respect your opinion. Death Note is a great anime, but it is not as good as Jujutsu Kaisen. Jujutsu Kaisen is the best anime of all time.")
@bot.command()
async def dragon_ball(ctx):
    await ctx.send("Dragon Ball is a classic anime, but it is not as good as Jujutsu Kaisen. Jujutsu Kaisen is the best anime of all time. But I can respect your opinion. Dragon Ball is a great anime, but it is not as good as Jujutsu Kaisen.")

@bot.command()
async def aot(ctx):
    await ctx.send("Attack on Titan is a great anime, but it is not as good as Jujutsu Kaisen. Jujutsu Kaisen is the best anime of all time. But I can respect your opinion. Attack on Titan is a great anime, but it is not as good as Jujutsu Kaisen.")
@bot.command()
async def my_little_sister_cant_be_this_cute(ctx):
    await ctx.send("bro just go away...")

@bot.command()
async def mem(ctx):
    with open('images/mem.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def geri_kullanım(ctx):
    await ctx.send("""- Şişeden ejderha: Pet şişeleri kesip boyayarak ejderha veya yaratık figürleri yapabilirsin. Alev efektini de renkli kağıt şeritlerle verirsin, harika olur!
- Klavye tuşlarından mozaik: Eski, bozuk klavyeler varsa tuşları söküp renk düzenine göre bir mozaik tablo tasarlayabilirsin—dijitalin sanata dönüşü!
- Plastik çatal ve kaşık ile uzaylı figürleri: Çatalları bacak, kaşıkları kafa gibi düşün. Biraz sıcak silikon, biraz hayal gücüyle evde küçük bir uzaylı istilası başlatabilirsin (sanatsal olanından tabii).
- CD kutularından ışıklı pano: Boş CD kutularını üst üste yerleştir, içine LED koy, dışını da plastik kapaklarla kapla. Hem retro hem cyberpunk bir hava yaratır.
- Kalemlik: İşine yaramayan veya gereksiz bir ilaç veya çöp bir cam şişesini al, üzerine resimler çiz, yapıştır ve dekore ettikten sonra daha geniş bir alan sunmak için altını kesip üstüne bant yapıştır
""")
@bot.command()
async def aferin(ctx):
    await ctx.send("Sağolun, size yardım etmek için buradayım !!!  :)")

@bot.command()
async def rastgelesayı(ctx, min: int = 1, max: int = 100):
    """Belirtilen aralıkta rastgele bir sayı üretir.""" #anlamadım ama yaptı bişeyler gene bu baya gelişti
    if min >= max:
        await ctx.send("Minimum değer maksimum değerden küçük olmalıdır.")
        return
    random_number = random.randint(min, max)
    await ctx.send(f"Rastgele sayı: {random_number}")
  
@bot.command()
async def info(ctx):
    await ctx.send("Merhaba ! Ben bir discord sohbet botuyum! bana soru sorabilirsin, benle sohbet edebilirsin ve beni sunucuna ekleyebilirsin ! ")

@bot.command()
async def oyuncubilgisayarı(ctx):
    await ctx.send("Oyuncu bilgisayarları genellikle yüksek performanslı işlemciler, güçlü grafik kartları, geniş RAM kapasitesi ve hızlı depolama birimleri ile donatılmıştır. Bu bileşenler, oyunların akıcı bir şekilde çalışmasını sağlar. Ayrıca, oyuncu bilgisayarlarında genellikle RGB aydınlatma, özel soğutma sistemleri ve estetik tasarımlar bulunur." \
    "işte sana örnek bir oyuncu bilgisayarı: " \
    "İşlemci: Intel Core i9-11900K\n" \
    "Anakart: ASUS ROG Strix Z590-E Gaming WiFi\n" \
    "RAM: Corsair Vengeance LPX 32GB (2 x 16GB) DDR5-3200\n" \
    "Grafik Kartı: NVIDIA GeForce RTX 5070 Ti\n" \
    "Depolama: Samsung 970 EVO Plus 1TB NVMe SSD\n" \
    "Güç Kaynağı: Corsair RM850x 850W 80+ Gold\n" \
    "Kasa: NZXT H510\n" \
    "Soğutma: Noctua NH-D15")



bot.run("ENTER BOT TOKEN HERE")  # Replace with your bot token








