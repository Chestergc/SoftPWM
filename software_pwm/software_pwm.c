#include <16f877.h>         // This is the header for the PIC i'm using
#device ADC=10              // Sets the ADC to be 10 bit wide
#use delay (clock=20000000) // sets the clock for 20MHz
#include <cuscostdio.h>     // This is the standard library for the board

main()       //
  {
  int s1 = 0b10101010;
  int s2 = 0x00;
  int s;
  int t1, I;
  long aux = 0;
  output_a(0);  // resets A PORTS
  output_b(0);  // resets B PORTS
  output_c(0);  // resets C PORTS
  output_d(0);  // resets D PORTS
  while(1)         // loop
    {
    if (aux == 1000) s = s2;   // changes into hex
    if (aux == 2000)           // changes into binary, resets aux
       {
       s = s1;
       aux = 0;
       }
    delay_us(5);
    output_d(s);
    output_c(~s);
    t1 ++;
    if (t1 == 0) s = ~s;      // inverting the signal
    if (s & 0b00000001) output_high(BUZZER);  // ????
    else                output_low(BUZZER);   // ????
    if (t1 == I)              // figure out the end of the duty cicle
       {
       s = ~s;
       I --;
       aux ++;
       }
    }
  }
