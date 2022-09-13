#include "crow.h"

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/").methods("POST"_method)
    ([](const crow::request &req)
     {
         auto data = crow::json::load(req.body);
         if (!data)
             return crow::response(400);
     });

    app.port(18080).multithreaded().run();
}