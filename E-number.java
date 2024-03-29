import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.math.*;

import javax.tools.Tool;

public class Irrationals {

	public static void main(String args[]) {
		BigDecimal eNumber = new BigDecimal("0"), precision = new BigDecimal("1500");

		for (BigDecimal i = BigDecimal.valueOf(0); i.compareTo(precision) <= 0; i = i.add(BigDecimal.ONE)) {
			BigDecimal res = BigDecimal.ONE.divide(factorial(i), new MathContext(100, RoundingMode.HALF_UP));
			eNumber = eNumber.add(res);
		}

		System.out.print(eNumber.toString());
	}
}
