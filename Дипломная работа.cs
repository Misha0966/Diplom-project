using System;

class Program
{
    static void Main()
    {
        double r = 0.26;  // радиус муравейника
        double h = 0.12;  // высота муравейника
        double Vn = ((Math.PI * h) / 6) * (3 * r * r + h * h);  // объем наземной части муравейника, где r - радиус муравейника, а h - его высота
        double Vp = 2.0 / 3.0 * Vn;  // объем поземной части муравейника
        double Vreal = Vn + Vp;  // где Vn - объем наземной части, а Vp - объем поземной части

        Console.WriteLine("Общий объем муравейника: " + Vreal);

        // Определим размер выборки
        double[] measurements = { 0.003, 0.003, 0.003, 0.003, 0.01, 0.003, 0.004, 0.003, 0.004, 0.003 };
        double Na = 0;
        foreach (var measurement in measurements)
        {
            Na += measurement;
        }
        Na /= 10.0;
        Console.WriteLine("Размер выборки: " + Na);

        // Определим объём выборки
        double VNa = Na * Math.Pow(10, -6);
        Console.WriteLine("Объем выборки: " + VNa);

        // Определим кол-во муравьёв, живущих в муравейнике
        double x = (Vreal / VNa) / 10.0;
        int roundedX = (int)Math.Round(x);
        Console.WriteLine("Общее количество муравьев: " + roundedX);
    }
}
