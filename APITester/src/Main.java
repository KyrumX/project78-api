import Tests.GetTests;
import Tests.PostTests;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Main {

    public static void main(String[] args) throws Exception {
        GetTests getTests = new GetTests();
        GetTests.getTest("http://86.82.103.122:8080/api/orders/");
        GetTests.getTest("http://86.82.103.122:8080/api/orders/1");

        //  Create a new order
        Date mydate = new Date();
        DateFormat df = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        String mydateStr = df.format(mydate);

        String urlParameters = "tablenumber=487&datetime="+mydateStr+"";

        PostTests.postTest("http://86.82.103.122:8080/api/orders/", urlParameters);

        //Create a new orderline

        PostTests.postTest("http://86.82.103.122:8080/api/orderlines/", "amount=2&menuitem=1&orderid=10");
    }
}
