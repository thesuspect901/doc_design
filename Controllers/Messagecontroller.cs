using Microsoft.AspNetCore.Mvc;
using lab3_doc_design.Models;
using System.Linq;
using System;
using System.Collections.Generic;

namespace lab3_doc_design.Controllers
{
    public class MessageController : Controller
    {
        private static List<Message> messages = new List<Message>();

        // LIST
        public IActionResult Index()
        {
            return View(messages);
        }

        // CREATE GET
        public IActionResult Create()
        {
            return View();
        }

        // CREATE POST
        [HttpPost]
        public IActionResult Create(Message message)
        {
            message.Id = messages.Count + 1;
            message.Timestamp = DateTime.Now;

            messages.Add(message);

            return RedirectToAction("Index");
        }

        // DELETE
        public IActionResult Delete(int id)
        {
            var msg = messages.FirstOrDefault(x => x.Id == id);

            if (msg != null)
                messages.Remove(msg);

            return RedirectToAction("Index");
        }

        // EDIT GET
        public IActionResult Edit(int id)
        {
            var msg = messages.FirstOrDefault(x => x.Id == id);
            return View(msg);
        }

        // EDIT POST
        [HttpPost]
        public IActionResult Edit(Message message)
        {
            var msg = messages.FirstOrDefault(x => x.Id == message.Id);

            if (msg != null)
            {
                msg.UserName = message.UserName;
                msg.Text = message.Text;
                msg.ChatId = message.ChatId;
            }

            return RedirectToAction("Index");
        }
    }
}