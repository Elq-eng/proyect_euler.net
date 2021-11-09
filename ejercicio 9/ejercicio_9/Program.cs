using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ejercicio_9
{
    class Program
    {
        static void Main(string[] args)
        {

            int total = 0;
            int value = 1001;
            int response = 0;
            int c = 0;
            int result = 0;
            int variable = 0;

            for(int a = 0; a <= value; a++)
            {
                for(int b = 0; b <= value; b++)
                {
                    c = NewMethod(value, a, b);
                    result = (int)(Math.Pow(a, 2) + Math.Pow(b, 2));
                    variable = (int)(Math.Pow(c,2));
                    if(variable == result)
                    {
                        total = a + b + c;
                        if (total == 1000)
                        {
                            response = a * b * c;
                            Console.WriteLine(Convert.ToString(response));
                            /*Console.WriteLine(Int32.Parse(response));*/
                        }

                    }
                }
            }

        }

        public static int NewMethod(int value, int a, int b)
        {

            return (value - 1) - a - b; ;
        }
    }
}
