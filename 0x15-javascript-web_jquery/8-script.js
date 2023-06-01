$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, status){
    const movies = data.results;
    $.each(movies, function(index, val){
        item = $("<li></li>").text(val.title);
        $("#list_movies").append(item);
    });
});