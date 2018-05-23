package Tests;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class PostTests {
    public static void postTest(String url, String body) throws Exception {
        //Code is based on the frame provided by mkyong: https://www.mkyong.com/java/how-to-send-http-request-getpost-in-java/

        System.out.println();
        System.out.println("Starting a new POST test:");

        URL object = new URL(url);
        HttpURLConnection connection = (HttpURLConnection) object.openConnection();

        connection.setRequestMethod("POST");
        connection.setRequestProperty("User-Agent", "Mozilla/5.0");
        connection.setRequestProperty("Accept", "application/json");

        Date mydate = new Date();
        DateFormat df = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        String mydateStr = df.format(mydate);

        String urlParameters = "tablenumber=111&datetime="+mydateStr+"";

        // Send post request
        connection.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(connection.getOutputStream());
        wr.writeBytes(urlParameters);
        wr.flush();
        wr.close();

        int responseCode = connection.getResponseCode();
        System.out.println("\nSending 'POST' request to URL : " + url);
        System.out.println("Post parameters : " + urlParameters);
        System.out.println("Response Code : " + responseCode);


        InputStreamReader inputStreamReader = new InputStreamReader(connection.getInputStream());
        if (responseCode != 201) {
            inputStreamReader = new InputStreamReader(connection.getErrorStream());
        }

        BufferedReader in = new BufferedReader(inputStreamReader);
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        //print result
        System.out.println(response.toString());

    }
}
