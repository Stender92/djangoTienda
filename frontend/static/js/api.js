$(document).ready(
    function(){
        $.get("https://fakestoreapi.com/products/category/jewelery",
            function(data){
                $.each(data, function(id,values){
                    $("#cards").append(`
                    <div class="col mb-5">
                    <div class="card h-100">
                        <!-- Sale badge-->
                        <div class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem">Sale</div>
                        <!-- Product image-->
                        <img class="card-img-top" src="${values.image}" alt="..."/>
                        <!-- Product details-->
                        <div class="card-body p-4">
                            <div class="text-center">
                                <!-- Product name-->
                                <h5 class="fw-bolder">${values.title}</h5>
                                </br>${values.category}
                                <!-- Product reviews-->
                                <div class="d-flex justify-content-center small text-warning mb-2">
                                    <div class="bi-star-fill">${values.rating.rate}</div>
                                </div>
                                <!-- Product price-->
                                <span class="text-muted text-decoration-line-through">$999.999</span>
                                $${values.price}
                            </div>
                        </div>
                        <!-- Product actions-->
                        <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                            <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="#">Añadir</a></div>
                        </div>
                    </div>
                </div>`)
                        
                })
                    
            }
            )
                
        } 
);

$(document).ready(
    function(){
        $.get("https://fakestoreapi.com/products/category/electronics",
            function(data){
                $.each(data, function(id,values){
                    $("#cards2").append(`
                    <div class="col mb-5">
                    <div class="card h-100">
                        <!-- Sale badge-->
                        <div class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem">Sale</div>
                        <!-- Product image-->
                        <img class="card-img-top" src="${values.image}" alt="..."/>
                        <!-- Product details-->
                        <div class="card-body p-4">
                            <div class="text-center">
                                <!-- Product name-->
                                <h5 class="fw-bolder">${values.title}</h5>
                                </br>${values.category}
                                <!-- Product reviews-->
                                <div class="d-flex justify-content-center small text-warning mb-2">
                                    <div class="bi-star-fill">${values.rating.rate}</div>
                                </div>
                                <!-- Product price-->
                                <span class="text-muted text-decoration-line-through">$999.999</span>
                                $${values.price}
                            </div>
                        </div>
                        <!-- Product actions-->
                        <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                            <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="#">Añadir</a></div>
                        </div>
                    </div>
                </div>`)
                        
                })
                    
            }
            )
                
        } 
);


$(document).ready(
    function(){
        $.get("https://fakestoreapi.com/products/category/men's%20clothing",
            function(data){
                $.each(data, function(id,values){
                    $("#cards3").append(`
                    <div class="col mb-5">
                    <div class="card h-100">
                        <!-- Sale badge-->
                        <div class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem">Sale</div>
                        <!-- Product image-->
                        <img class="card-img-top" src="${values.image}" alt="..."/>
                        <!-- Product details-->
                        <div class="card-body p-4">
                            <div class="text-center">
                                <!-- Product name-->
                                <h5 class="fw-bolder">${values.title}</h5>
                                </br>${values.category}
                                <!-- Product reviews-->
                                <div class="d-flex justify-content-center small text-warning mb-2">
                                    <div class="bi-star-fill">${values.rating.rate}</div>
                                </div>
                                <!-- Product price-->
                                <span class="text-muted text-decoration-line-through">$999.999</span>
                                $${values.price}
                            </div>
                        </div>
                        <!-- Product actions-->
                        <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                            <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="#">Añadir</a></div>
                        </div>
                    </div>
                </div>`)
                        
                })
                    
            }
            )
                
        } 
);


$(document).ready(
    function(){
        $.get("https://fakestoreapi.com/products/category/women's%20clothing",
            function(data){
                $.each(data, function(id,values){
                    $("#cards4").append(`
                    <div class="col mb-5">
                    <div class="card h-100">
                        <!-- Sale badge-->
                        <div class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem">Sale</div>
                        <!-- Product image-->
                        <img class="card-img-top" src="${values.image}" alt="..."/>
                        <!-- Product details-->
                        <div class="card-body p-4">
                            <div class="text-center">
                                <!-- Product name-->
                                <h5 class="fw-bolder">${values.title}</h5>
                                </br>${values.category}
                                <!-- Product reviews-->
                                <div class="d-flex justify-content-center small text-warning mb-2">
                                    <div class="bi-star-fill">${values.rating.rate}</div>
                                </div>
                                <!-- Product price-->
                                <span class="text-muted text-decoration-line-through">$999.999</span>
                                $${values.price}
                            </div>
                        </div>
                        <!-- Product actions-->
                        <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                            <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="#">Añadir</a></div>
                        </div>
                    </div>
                </div>`)
                        
                })
                    
            }
            )
                
        } 
);