from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conversa = ['Oi', 'Olá', 'Tudo Bem?', 'Eu estou bem']
conversa2 = ['Qual o seu filme preferido?', 'Projeto X']
conversa3 = ['Quantos anos voce tem?', 'Menos de 1 Mês']

bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(conversa2)
bot.train(conversa3)

while True:
	quest = input("Você: ")
	resposta = bot.get_response(quest)
	if float(resposta.confidence) > 0.5:
		print ('Bot:', resposta)
	else:
		print ('Bot: Eu não sei')