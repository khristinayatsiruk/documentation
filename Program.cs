using Microsoft.EntityFrameworkCore; // Потрібно для UseInMemoryDatabase
using MusicEventsApp.Data;         // Потрібно, щоб бачити твій ApplicationDbContext

var builder = WebApplication.CreateBuilder(args);

// 1. Реєструємо сервіс Контролерів та Views (вже було)
builder.Services.AddControllersWithViews();

// 2. ДОДАЄМО БАЗУ ДАНИХ (це серце твоєї лаби)
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseInMemoryDatabase("MusicEventsDb"));

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();
app.UseAuthorization();

// 3. Налаштування маршруту (вже було)
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();