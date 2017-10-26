# Projeto 3

Por Pedro de la Peña e Daniel Ruhman

## Modulação Digital

### Funcionamento geral

O projeto consiste na transmissão de dados entre dois computadores por meio de da modulação de sinais pelo transmissor seguida pela desmodulação no receptor. O envio de dados é feito com base em uma caixa de texto, na qual o usuário pode escrever o que bem entender, e uma interface que exibe os dados enviados e recebidos.
A modulação e demodulação são feitas no software GNU Radio enquanto a interface foi feita em python.

#### Envio do dado

Após o usuário digitar uma mensagem na interface, o dado é enviado ao GNU Radio que, por sua vez, agrupa os bytes da mensagem e os transforma em um sinal.

#### Recepção do dado

O sinal captado pelo receptor é transformado em bytes que são reconhecidos e convertidos em strings. Caso ocorra alguma falha na transmissão, não há reenvio e o dado é perdido.

## Frequencia de transmissão e bandas utilizadas

Para o envio e receoção, foram utilizadas frequências de 2.2kHz, com banda igual a duas vezes a frequẽncia, ou seja, 4.4kHz.

## Modulação BPSK

A modulação BPSK é realizada alterando a fase de um sinal e mantendo sua frequência e amplitude constantes.
