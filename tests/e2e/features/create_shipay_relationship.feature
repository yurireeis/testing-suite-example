# language: pt
@criar_relacionamento_shipay
Funcionalidade: Criar um relacionamento com o Shipay
  Como um usuário interessado em integrar no sistema de frente de caixa um hub das principais ferramentas do mercado, como PicPay, Mercado Pago, Ame, Pag Bank, PIX, entre outras
  Para que possa me destacar no mercado e atender os meus clientes com maior comodidade
  Quero encontrar uma forma de contato com o Shipay

  Contexto: usuário acessa a página do negócio
    Dado que o usuário acessa a página do negócio

  @contato_fale_conosco
  Cenário: Iniciar um contato através do fale conosco
    Dado que iniciou o processo de falar com a equipe do shipay
    Quando informar os dados necessários para iniciar o relacionamento
    Então deverá receber a informação de que a requisição foi realizada com sucesso
