#include <16f877.h>         // This is the header for the PIC i'm using
#device ADC=10              // Sets the ADC to be 10 bit wide
#use delay (clock=20000000) // sets the clock for 20MHz
#include <cuscostdio.h>     // This is the standard library for the board

main(){
  output_a(0x00);
  output_b(0x00);
  output_c(0x00);
  output_d(0x00);

  while(1){
    if (aux == 1000) s = s2;   // changes into hex
    if (aux == 2000)           // changes into binary, resets aux
       {
       s = s1;
       aux = 0;
       }
    delay_us(5);
    t1 ++;
    if (t1 == 0) s = ~s;      // inverting the signal
    if (s & 0b00000001) output_high(BUZZER);  // buzzer out
    else                output_low(BUZZER);   // ????
    if (t1 == I)              // figure out the end of the duty cicle
       {
       s = ~s;
       I --;
       aux ++;
       }
  }

}
