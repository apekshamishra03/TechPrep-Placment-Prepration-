import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws Exception {
        Socket s = new Socket("localhost", 8000); // server ka address
        PrintWriter out = new PrintWriter(s.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));

        out.println("Hello Server!");
        System.out.println("Server says: " + in.readLine());

        s.close();
    }
}