## Bot de bate-papo baseado em AI 
Com algumas modificações, tive a ideia de subir todo o arquivo no github, já que meu projeto foi pausado e muitas pessoas ainda se interessavam a usar o meu bot, que infelizmente vou parado por um tempo, lá no telegram. Agradeço aqueles que me apoiaram.
Fiz mudanças no script, antes de subir aqui, por exemplo: Aqui, ele usa a inteligencia artificial da OPENAI, por meio da openai api, use seu token de api da openai para ter o bot funcionando.
Este projeto é um bot de bate-papo baseado em AI (Inteligência Artificial) que foi desenvolvido para ser usando noTelegram. Para que o bot funcione corretamente, é necessário que duas bibliotecas estejam instaladas no servidor, ou em seu pc: *openai e pytelegrambot*.

### Como instalar as bibliotecas com pip

Para instalar as bibliotecas necessárias, abra o terminal e digite o seguinte comando:
`pip install openai pyTelegramBotAPI`
caso esteja no linux, talvez seja necessario o uso do *pip3*

## Colete a sua Key da Openai
![Td8JdQT](https://user-images.githubusercontent.com/70298185/236633707-ec3dc77d-6dfa-4d76-b63f-1d99837804f6.png)


### Adicione suas informações no arquivo keys.py

![keys para github](https://user-images.githubusercontent.com/70298185/236688150-2ea0e040-40a8-48ab-a30c-83862cd0dcdb.png)

As informações, são necessaria para o funcionamento do bot, pois, sarão elas que dará o uso ao consumo das API's do telegram e da openai.
- Crie um bot dentro do botfather no telegram, pegue a api do mesmo e cole no campo: 
```token = 'YOUR BOT TOKEN_TELEGRAM'```

- E adicione a key da openai no campo:
```openai.api_key = 'YOUR OPENAI KEY'```

- Colete de alguma forma, o id da sua conta telegram, para que possa ter ações de administrador no bot, como o comando /on , que é especial aos admins
```admin = [YOUR ID TELEGRAM]```
Caso queira adicionar mais de um id, coloque uma virgula ao passar de um id para o outro (Caso não funcione, remova o espaço)
exemplo: admin = [999999, 555555, 111111] 


### Comando para usar o bot

![alterar comando github](https://user-images.githubusercontent.com/70298185/236688161-190993a4-66ad-4a02-baa1-c84e35402d29.png)


Altere o campo que contem a frase: "SEU COMANDO AQUI", para que este comando, possa ser o / que dará a ação ao bot dentro do telegram, em grupos.
exemplo: Fazer que o bot responda com /pergunta, ficaria assim com o campo alterado: 
```@bot.message_handler(commands=['pergunta'])```
Com isto, quando o usuario for usar o bot em grupos, o usuario terá que usar /pergunta, seguido da pergunta, exemplo:
/pergunta qual é a maior palavra do português



### Como usar o bot no Telegram
Após ter configurado suas informações no script: Execute o arquivo main.py usando o:
No Linux: `python3 main.py`
No Windows: `python main.py`
(Para deixar rodand em segundo plano, adicione o & no final do comando)
Encontre o bot e enviá-lo uma mensagem. Normalmente a primeira mensagem é o /start, com isto ele já vai mostrar algumas informações


#### Comandos 
![Sem título](https://user-images.githubusercontent.com/70298185/236633918-15431d10-380a-427d-86fe-f31afe2e1247.png)

- /start: inicie o bot e comece uma nova conversa
- /on: mostra a memória do servidor que o bot está (APENAS PARA ADMINS)
- /aide: use este comando em grupos para interagir com o bot e fazer perguntas
- Observação: quando a conversa é iniciada no chat privado do bot, não é necessário usar o comando /aide, basta enviar a mensagem e o bot irá responder como um ser humano em tempo real, incluindo efeitos de digitação.


### Funcionamento do Script
![Diagrama sem nome drawio](https://user-images.githubusercontent.com/70298185/236815765-aad7ec7a-b9f1-4a6e-9b9a-2f37ad23ce83.png)

***
### Modelo de Interpretação 
__*Leia a documentação para uso da api da openai*__
É disponibilidado 12 modelos ao todo, com diferentes tempos de respostas, e formas de interpretações diferentes.
acesse: [Documentação de modelo OpenAi](https://platform.openai.com/docs/models/gpt-3-5) para mais informações

### Tempo de Resposta

Modelo|tempo de resposta
---|---
davinci|4 segundos
curie|15 segundos
babbage| 90segundos
ada| 60segundos
cushman| 60segundos
davinci-instruct-beta| 6segundos
content-filter-alpha-c4| 4segundos
content-filter-dev| Desconhecido
davinci-codex| 50segundos
text-davinci-002| 5segundos
text-davinci-001| Desconhecido
text-curie-001| Desconhecido

### Alterando o modelo
Caso tenha a necessidade de alterar o modelo, faça a edição na parte `model` do script, disponiveis nos arquivos main.py e chatprivado.py

![code](https://user-images.githubusercontent.com/70298185/236867481-5c902d48-e625-4bb3-9086-27ffe8c42a2f.png)



[*Acesse a documentação de modelos, antes da mudança*](https://platform.openai.com/docs/models/overview)
Adicione o nome completo da versão que deseja, no campo `model`, exemplo com o modelo: gpt-3.5-turbo
![exemplo](https://user-images.githubusercontent.com/70298185/236867195-16ecc7aa-99c2-426a-9d10-b127e7231367.png)


***

Mantenha as conversas dentro dos tópicos adequados e respeite outras pessoas no grupo. Este projeto é desenvolvido apenas para fins educacionais e pode não ser adequado para determinadas aplicações comerciais ou outros fins. Por favor, explore o projeto como desejado e divirta-se! 
