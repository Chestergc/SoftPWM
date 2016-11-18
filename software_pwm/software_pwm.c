#include <16f877.h>         // identifica microcontrolador alvo
#device ADC=10              // define AD para 10 bits, variando de 0 a 1023
#use delay (clock=4000000)  // <- define cristal para 4Mhz. Para outros valores, mude e recompile.
#include <cuscostdio.h>     // inclui biblioteca de fun��es do projeto CUSCOPiC

main()       // fun��o principal
  {
  int s1 = 0b10101010;
  int s2 = 0x00;
  int s;
  int t1, I;
  long aux = 0;
  output_a(0);  // desliga todo PORTA
  output_b(0);  // desliga todo PORTB
  output_c(0);  // desliga todo PORTC
  output_d(0);  // desliga todo PORTD
  while(1)         // para repetir bloco. La�o infinito. tempo de ciclo de menos de um ms
    {
    if (aux == 1000) s = s2;   // muda para padr�o s2
    if (aux == 2000)           // muda para padr�o s1
       {
       s = s1;
       aux = 0;
       }
    delay_us(5);
    output_d(s);
    output_c(~s);
    t1 ++;
    if (t1 == 0) s = ~s;      // aqui inverte o sinal (inicio do ciclo)
    if (s & 0b00000001) output_high(BUZZER);  // buzzer
    else                output_low(BUZZER);   // sincronizado com bit menos significativo de s
    if (t1 == I)              // descobre quando � o final do pulso no ciclo (fim do duty cicle)
       {
       s = ~s;
       I --;
       aux ++;
       }
    }
  }
