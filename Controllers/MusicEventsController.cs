using Microsoft.AspNetCore.Mvc;
using MusicEventsApp.Data;
using MusicEventsApp.Models;

namespace MusicEventsApp.Controllers;

public class MusicEventsController : Controller
{
    private readonly ApplicationDbContext _context;

    public MusicEventsController(ApplicationDbContext context)
    {
        _context = context;
    }

    // 1. СПИСОК ПОДІЙ
    public IActionResult Index()
    {
        var events = _context.MusicEvents.ToList();
        return View(events);
    }

    // 2. СТВОРЕННЯ (ФОРМА)
    public IActionResult Create() => View();

    [HttpPost]
    public IActionResult Create(MusicEvent musicEvent)
    {
        _context.MusicEvents.Add(musicEvent);
        _context.SaveChanges();
        return RedirectToAction(nameof(Index));
    }

    // 3. РЕДАГУВАННЯ (ФОРМА)
    public IActionResult Edit(int id)
    {
        var musicEvent = _context.MusicEvents.Find(id);
        if (musicEvent == null) return NotFound();
        return View(musicEvent);
    }

    [HttpPost]
    public IActionResult Edit(MusicEvent musicEvent)
    {
        _context.MusicEvents.Update(musicEvent);
        _context.SaveChanges();
        return RedirectToAction(nameof(Index));
    }

    // 4. ВИДАЛЕННЯ
    public IActionResult Delete(int id)
    {
        var musicEvent = _context.MusicEvents.Find(id);
        if (musicEvent != null)
        {
            _context.MusicEvents.Remove(musicEvent);
            _context.SaveChanges();
        }
        return RedirectToAction(nameof(Index));
    }
}