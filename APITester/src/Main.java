import Tests.GetTests;
import Tests.PostTests;

public class Main {

    public static void main(String[] args) throws Exception {
        GetTests getTests = new GetTests();
        GetTests.getTest("http://127.0.0.1:8000/api/orders/");
        GetTests.getTest("http://127.0.0.1:8000/api/orders/1");
        PostTests.postTest("http://127.0.0.1:8000/api/orders/", "");
    }
}
