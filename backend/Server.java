import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.OutputStream;
import java.io.InputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

public class Server {
    public static void main(String[] args) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
        System.out.println("Server started at http://localhost:8000");

        server.createContext("/sendMessage", new MyHandler());
        server.setExecutor(null); // default executor
        server.start();
    }

    static class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            InputStream is = exchange.getRequestBody();
            byte[] data = is.readAllBytes();
            String message = new String(data, StandardCharsets.UTF_8);

            System.out.println("Message from frontend: " + message);

            String response = "Server received: " + message;
            exchange.sendResponseHeaders(200, response.getBytes().length);
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}